from typing import Any, List, Optional, Sequence

from sqlalchemy.sql import text, column

from sqlalchemy import func

from numpy import round as round_n

from .models import Ingredient, Order, OrderDetail, Size, db, Beverage
from .serializers import (
    IngredientSerializer,
    OrderSerializer,
    SizeSerializer,
    BeverageSerializer,
    ma,
)


class BaseManager:
    model: Optional[db.Model] = None
    serializer: Optional[ma.SQLAlchemyAutoSchema] = None
    session = db.session

    @classmethod
    def get_all(cls):
        serializer = cls.serializer(many=True)
        _objects = cls.model.query.all()
        result = serializer.dump(_objects)
        return result

    @classmethod
    def get_by_id(cls, _id: Any):
        entry = cls.model.query.get(_id)
        return cls.serializer().dump(entry)

    @classmethod
    def create(cls, entry: dict):
        serializer = cls.serializer()
        new_entry = serializer.load(entry)
        cls.session.add(new_entry)
        cls.session.commit()
        return serializer.dump(new_entry)

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        cls.session.query(cls.model).filter_by(_id=_id).update(new_values)
        cls.session.commit()
        return cls.get_by_id(_id)


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return (
            cls.session.query(cls.model)
            .filter(cls.model._id.in_(set(ids)))
            .all()
            or []
        )


class OrderManager(BaseManager):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(
        cls,
        order_data: dict,
        ingredients: List[Ingredient],
        beverages: List[Beverage],
    ):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all(
            (
                OrderDetail(
                    order_id=new_order._id,
                    ingredient_id=ingredient._id,
                    ingredient_price=ingredient.price,
                    total_detail_price=ingredient.price,
                )
                for ingredient in ingredients
            )
        )
        cls.session.add_all(
            (
                OrderDetail(
                    order_id=new_order._id,
                    beverage_id=beverage._id,
                    beverage_price=beverage.price,
                    total_detail_price=beverage.price,
                )
                for beverage in beverages
            )
        )
        cls.session.commit()
        return cls.serializer().dump(new_order)

    @classmethod
    def update(cls):
        raise NotImplementedError(f"Method not suported for {cls.__name__}")


class IndexManager(BaseManager):
    @classmethod
    def test_connection(cls):
        cls.session.query(column("1")).from_statement(text("SELECT 1")).all()


class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return (
            cls.session.query(cls.model)
            .filter(cls.model._id.in_(set(ids)))
            .all()
            or []
        )


class ReportManager:
    session = db.session

    @classmethod
    def get_most_requested_ingredient(cls):
        return (
            cls.session.query(
                Ingredient, func.count(OrderDetail.ingredient_id)
            )
            .join(OrderDetail)
            .group_by(Ingredient)
            .order_by(func.count(OrderDetail.ingredient_id).desc())
            .first()
        )

    @classmethod
    def get_most_requested_beverage(cls):
        return (
            cls.session.query(Beverage, func.count(OrderDetail.beverage_id))
            .join(OrderDetail)
            .group_by(Beverage)
            .order_by(func.count(OrderDetail.beverage_id).desc())
            .first()
        )

    @classmethod
    def get_month_with_more_revenue(cls):
        return (
            cls.session.query(Order.date, func.sum(Order.total_price))
            .group_by(Order.date)
            .order_by(func.sum(Order.total_price).desc())
            .first()
        )

    @classmethod
    def get_top_three_customers(cls):
        return (
            cls.session.query(Order, func.sum(Order.total_price))
            .group_by(Order.client_dni)
            .order_by(func.sum(Order.total_price).desc())
            .limit(3)
            .all()
            or []
        )

    @classmethod
    def get_report(cls):
        most_requested_ingredient = cls.get_most_requested_ingredient()
        most_requested_beverage = cls.get_most_requested_beverage()
        month_with_more_revenue = cls.get_month_with_more_revenue()
        top_three_customers = cls.get_top_three_customers()

        return {
            "most_requested_ingredient": {
                "name": most_requested_ingredient[0].name,
                "times_requested": most_requested_ingredient[1],
            },
            "most_requested_beverage": {
                "name": most_requested_beverage[0].name,
                "times_requested": most_requested_beverage[1],
            },
            "month_with_more_revenue": {
                "name": month_with_more_revenue[0].strftime("%B"),
                "total_revenue": round_n(month_with_more_revenue[1], 2),
            },
            "top_3_customers": [
                {
                    "dni": customer[0].client_dni,
                    "name": customer[0].client_name,
                    "address": customer[0].client_address,
                    "phone": customer[0].client_phone,
                    "spent": round_n(customer[1], 2),
                }
                for customer in top_three_customers
            ],
        }

# from typing import Any, List

# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session

# from app import schemas, crud

# from app.schemas import product as product_schema
# from app.schemas import message as message_schema
# from app.api.deps import get_db

# router = APIRouter()


# @router.get("", response_model=List[product_schema.ProductResponse])
# def read_products(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
#     """
#     Retrieve all products.
#     """
#     products = crud.product.get_multi(db, skip=skip, limit=limit)
#     return products


# @router.post("", response_model=product_schema.ProductResponse)
# def create_product(*, db: Session = Depends(get_db), product_in: product_schema.ProductCreate) -> Any:
#     """
#     Create new products.
#     """
#     product = crud.product.create(db, obj_in=product_in)
#     return product


# @router.put("", response_model=product_schema.ProductResponse)
# def update_product(*, db: Session = Depends(get_db), product_in: product_schema.ProductUpdate) -> Any:
#     """
#     Update existing products.
#     """
#     product = crud.product.get(db, model_id=product_in.id)
#     if not product:
#         raise HTTPException(
            # status.HTTP_,
#             detail="The product with this ID does not exist in the system.",
#         )
#     product = crud.product.update(db, db_obj=product, obj_in=product_in)
#     return product


# @router.delete("", response_model=message_schema.Message)
# def delete_product(*, db: Session = Depends(get_db), id: int) -> Any:
#     """
#     Delete existing product.
#     """
#     product = crud.product.get(db, model_id=id)
#     if not product:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="The product with this ID does not exist in the system.",
#         )
#     crud.product.remove(db, model_id=product.id)
#     return {"message": f"Product with ID = {id} deleted."}

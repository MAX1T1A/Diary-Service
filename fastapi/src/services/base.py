from sqlalchemy.orm import Session


def create_items(db: Session, db_item):
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

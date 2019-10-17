name_table= ( 'names' ,db.metadata,
            Column('id', Integer , primary_key=True),
            Column('product_id', Integer , ForeignKey(products.id)),
            Column('name', String(255)),
            )
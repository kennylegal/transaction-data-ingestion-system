import psycopg2

def create_db(cur, conn):
    cur.execute(
        """
    create table if not exists Users(
        user_id  serial primary key,
        username varchar(200),
        email varchar(100),
        phone varchar (50),
        gender varchar (10),
        age int,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );""")

    cur.execute(
        """
    create table if not exists wallets (
        id serial primary key,
        user_id serial,
        currency varchar(10),
        balance bigint,
        updated_at timestamp default current_timestamp,

        foreign key (user_id) references users(user_id)
        );
        """
    )

    cur.execute(
        """
    create table if not exists transactions (
        id serial primary key,
        user_id serial,
        type varchar(10),
        amount bigint,
        status varchar(20),
        updated_at timestamp default current_timestamp,

        foreign key (user_id) references users(user_id)
        );
        """
    )
    conn.commit()



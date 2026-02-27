import psycopg2

def create_db(cur):
    cur.execute(
        """
    create table if not exists Users(
        user_id  serial primary key,
        email varchar(50),
        phone varchar (12),
        kyc_status bool,
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
    
def populate_table(cur, ):
    pass

if __name__ == "__main__":
    conn = psycopg2.connect(
        database="wallet_project",
        user="admin",
        password="mydb",
        host="localhost",
        port="5435"
    )
    cur = conn.cursor()
    create_db(cur)
    conn.commit()

    cur.close()
    conn.close()
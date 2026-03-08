def populate_table(cur):
    cur.execute("""
    INSERT INTO users(email, phone, kyc_status)
    VALUES('legalkenny02@gmail.com', '08164647584', true);
    """)


def updated_trigger(cur):

    cur.execute("""
    create or replace function update_updated_at_column ()
            returns trigger as $$
                begin
                    NEW.updated_at = current_timestamp;
                    return NEW;
                end;
            $$ language plpgsql;
    """)
    cur.execute("""

            create trigger set_updated_at
            before update on users
            for each row
            execute function update_updated_at_column();
        """)
    return None

def update_table(cur):
    cur.execute("""
    UPDATE users
    SET email = 'badboysgeng@gmail.com'
    where user_id = 3
    """)
    return None
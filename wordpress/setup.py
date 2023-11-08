from sqlalchemy import create_engine, text


def clear_database(connection):
    # reset all wordpress dabase and tabeles
    drop_user_sql = "DROP USER IF EXISTS 'wordpress'@'localhost';"
    connection.execute(text(drop_user_sql))
    drop_database_sql = "DROP DATABASE IF EXISTS `wordpress`;"
    connection.execute(text(drop_database_sql))


def create_database(connection):
    # create new wordpress dabase and tabeles
    create_database_sql = text("CREATE DATABASE wordpress CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;")
    connection.execute(create_database_sql)
    create_user_sql = text(
        ("CREATE USER 'wordpress'@'localhost' IDENTIFIED VIA mysql_native_password USING PASSWORD('wordpress'); ")
    )
    connection.execute(create_user_sql)
    grant_user_sql = text(
        (
            "GRANT USAGE ON *.* TO 'wordpress'@'localhost' REQUIRE NONE WITH "
            "MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;"
        )
    )
    connection.execute(grant_user_sql)


def uninstall_wp():
    # un-install all wp installations
    pass


def install_wp():
    pass


def main():
    connection_string = "mysql+mysqlconnector://root@localhost:3306/"
    engine = create_engine(connection_string, echo=True)

    with engine.connect() as connection:
        clear_database(connection)
        create_database(connection)
        connection.commit()

    uninstall_wp()
    install_wp()


if __name__ == "__main__":
    main()

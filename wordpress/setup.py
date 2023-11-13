from sqlalchemy import create_engine, text
from settings import WORDPRESS_ZIP_FILE
import zipfile
import os
import shutil


def clear_database(connection):
    # remove wordpress database
    drop_database_sql = "DROP DATABASE IF EXISTS `wordpress`;"
    connection.execute(text(drop_database_sql))


def create_database(connection):
    # create new wordpress dabase
    create_database_sql = text("CREATE DATABASE wordpress CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;")
    connection.execute(create_database_sql)

    # TODO: import tables from wordpress.sql
    # TODO: instead create new export with woocommerce extensions installed and products texes etc created


def uninstall_wp():
    wordpress_dir = os.path.join(WORDPRESS_ZIP_FILE.split(".zip")[0])

    print("Removing", wordpress_dir)
    shutil.rmtree(wordpress_dir)


def install_wp():
    wordpress_base_dir = os.path.dirname(WORDPRESS_ZIP_FILE)

    print("Extracting", WORDPRESS_ZIP_FILE, "to", wordpress_base_dir)
    with zipfile.ZipFile(WORDPRESS_ZIP_FILE, "r") as zip_ref:
        zip_ref.extractall(wordpress_base_dir)

    # TODO: create a new zip with wp initialized and woocommerce installed


# TODO: create a new backup of current wp setup
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

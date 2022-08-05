from mms.db import init_db, Session

def init():
    db = Session()
    print("Initializing database")
    init_db(db)
    print("Finished Initializing database")
    

def main():
    init()
    

if __name__ == '__main__':
    main()
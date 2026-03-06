from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, CheckConstraint, insert, select, update, delete
from sqlalchemy.exc import OperationalError

# Create database connection
# Note: Replace user, password, host, and database name with your actual MySQL credentials
DATABASE_URL = "mysql+pymysql://root:root@127.0.0.1/student_db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Create students table
students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('age', Integer, CheckConstraint('age >= 18')),
    Column('city', String(255), nullable=True)
)

def run_operations():
    try:
        # Create table in the database
        metadata.create_all(engine)
        print("Students table created successfully.")
        
        with engine.connect() as conn:
            # Clear existing data for a clean run if table already existed
            conn.execute(delete(students))
            conn.commit()

            # Insert 3 student records
            print("\n--- Inserting Records ---")
            insert_stmt = insert(students).values([
                {"name": "Rahul", "age": 20, "city": "Delhi"},
                {"name": "Priya", "age": 22, "city": "Mumbai"},
                {"name": "Amit", "age": 19, "city": "Pune"}  # Amit is < 20
            ])
            conn.execute(insert_stmt)
            conn.commit()
            print("Successfully inserted 3 student records.")
            
            # Fetch all students
            print("\n--- Fetching All Students ---")
            select_stmt = select(students)
            result = conn.execute(select_stmt)
            for row in result:
                print(dict(row._mapping))
            
            # Update city of student whose name = "Rahul"
            print("\n--- Updating Rahul's City ---")
            update_stmt = update(students).where(students.c.name == 'Rahul').values(city='Bangalore')
            conn.execute(update_stmt)
            conn.commit()
            print("Successfully updated Rahul's city.")
            
            # Delete student whose age < 20
            print("\n--- Deleting Students Age < 20 ---")
            delete_stmt = delete(students).where(students.c.age < 20)
            conn.execute(delete_stmt)
            conn.commit()
            print("Successfully deleted student(s) with age < 20.")
            
            # Final fetch to see the result
            print("\n--- Final Students List ---")
            final_result = conn.execute(select_stmt)
            for row in final_result:
                print(dict(row._mapping))
                
    except OperationalError as e:
        print("\n[Error] Unable to connect to MySQL database.")
        print("Please ensure your MySQL server is running, the database 'student_db' exists,")
        print("and the DATABASE_URL credentials are correct.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    run_operations()

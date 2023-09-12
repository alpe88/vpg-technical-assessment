import subprocess

# Database name to create
new_database_name = "vpg_test"

print("Creating the database...")
subprocess.run(["python", "test_utils/create.py", new_database_name])

print("Seeding the database...")
subprocess.run(["python", "test_utils/seed.py", new_database_name])

print("Setup completed.")

print("Running assesment script")
subprocess.run(["python", "Python_Program.py", new_database_name])

print("Deleting the database...")
subprocess.run(["python", "test_utils/delete.py", new_database_name])

print("Delete completed.")

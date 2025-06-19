## Superheroes API
**Phase 4  Code Challenge**

## **Description**
This is a RESTful API developed using Flask that enables seamless management of superheroes and their unique abilities. With this API, users can explore a list of heroes, update power descriptions, and assign strengths of various powers to different heroes. 


## Features

- View all heroes (GET /heroes)
- View individual hero with powers (GET /heroes/<id>)
- View all powers (GET /powers)
- Update a power’s description (PATCH /powers/<id>)
- Assign a power to a hero (POST /hero_powers)
- Proper validation and error handling






## Setup Instructions 

### **Requirements**
- Before setting up the project, ensure you have the following installed:

    - Python / Flask

    - SQLAlchemy / Flask-Migrate

    - SQLite

    

### Getting Started 
1. **Clone the repository**   
Open your terminal and run the following command:
    ```sh
    $git clone https://github.com/awuorochelle75/superheroes.git



2. **Navigate to the project folder**
    ```sh
        $cd superheoroes

3. **Install dependencies**
    ```sh
        $pipenv install flask flask_sqlalchemy flask_migrate


4. **Create virtual environment**
    ```sh
        $pipenv shell


5. **Set up your environment and database**

    ```sh
        $flask db init
        flask db migrate -m "Initial migration"
        flask db upgrade
        python -m app.seed  


6. **Run the server**

    ```sh
        $flask run
        

7.you can check http://localhost:5000/heroes to test


## API Testing
- Use Postman to test the provided endpoints.


## Contact Information
 Email: awuorochelle@gmail.com

## License
 MIT License @2025 Rochelle Awuor



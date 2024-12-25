Here’s the updated guide for running the project locally, including running npm run build before starting the Django server:

How to Run the Django + React Project Locally

1. Prerequisites

Make sure you have the following installed on your system:
	•	Python 3.8+
	•	Node.js 14+
	•	PostgreSQL (optional if you’re using SQLite for local development)

2. Clone the Repository

	1.	Open your terminal or command prompt.
	2.	Run the following command to clone the repository:

    ```
    git clone -b django-test https://github.com/kareemmosalah/SWE-project.git
3.	Navigate into the project directory:
   
    ```
    cd SWE-project
3. Frontend (React) Setup

	1.	Navigate to the front-end directory:
    
    ```
    cd myproject/front-end
  2.	Install the frontend dependencies:

    npm install
  3.	Build the React app for production:

    npm run build
This will generate the static files required to serve the React app from Django in the build directory.

4. Backend (Django) Setup

	1.	Navigate to the myproject directory:
    
    ```
    cd ../


2.	Create a virtual environment for Python:
   
    ```
    python -m venv myenv


4.	Activate the virtual environment:
	•	On Linux/Mac:
    ```
    source myenv/bin/activate

  •	On Windows:

    myenv\Scripts\activate

4.	Install the backend dependencies:
    ```
    pip install -r requirements.txt

5.	Set up the database:
    ```
    python manage.py migrate


6.	Start the Django development server:
    ```
    python manage.py runserver

The backend will now serve the React app at http://127.0.0.1:8000/.

5. Access the Application

	•	Open a browser and go to http://127.0.0.1:8000/.
	•	This will load the Django server, which serves the built React frontend.

6. Notes for Local Development

	•	Frontend Changes:
	•	If you make changes to the React code, you’ll need to rebuild the app:
    ```
    cd myproject/front-end
    npm run build


•	After rebuilding, restart the Django server for the changes to take effect.

•	Backend Changes:
•	If you make changes to the Django code, restart the Django server by pressing Ctrl+C in the terminal and running:

    python manage.py runserver


•	Environment Variables:
•	For sensitive information like SECRET_KEY or database credentials, use a .env file. Ensure your settings.py uses django-environ to load environment variables.



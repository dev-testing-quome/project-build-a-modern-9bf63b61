# Developer Setup Guide - project-build-a-modern

## Prerequisites

This guide assumes basic familiarity with command-line interfaces, Git, and at least one programming language (Python and JavaScript are used in this project).

**Required Software Versions:**

* **Docker:** 20.10.0 or higher (for Docker Option)
* **Docker Compose:** 1.29.0 or higher (for Docker Option)
* **Node.js:** 16.x or higher (for both options)
* **Python:** 3.9 or higher (for both options)
* **PostgreSQL:** 14 or higher (or compatible version specified in `docker-compose.yml` if using Docker)


**Development Tools:**

* **Git:** For version control.
* **Text Editor/IDE:** VS Code, Sublime Text, Atom, PyCharm, WebStorm (recommendations below).

**IDE Recommendations and Configurations:**

* **VS Code:** Highly recommended for its versatility and extensions for both frontend (JavaScript) and backend (Python) development. Install the following extensions:
    * Python
    * Prettier (for code formatting)
    * ESLint (for linting JavaScript)
    * Docker


## Local Development Setup

### Option 1: Docker Development (Recommended)

This option simplifies setup by encapsulating all dependencies within Docker containers.

1. **Clone Repository:**
   ```bash
   git clone <repository_url>
   cd project-build-a-modern
   ```

2. **Docker Setup:** Ensure Docker and Docker Compose are installed and running.

3. **Development Docker Compose Configuration:**  The project should include a `docker-compose.yml` file. This file defines the services (database, backend, frontend).  Example:

   ```yaml
   version: "3.9"
   services:
     db:
       image: postgres:14
       ports:
         - "5432:5432"
       environment:
         - POSTGRES_USER=your_db_user
         - POSTGRES_PASSWORD=your_db_password
         - POSTGRES_DB=your_db_name
     backend:
       build: ./backend
       ports:
         - "8000:8000"
       depends_on:
         - db
       environment:
         - DATABASE_URL=postgres://your_db_user:your_db_password@db:5432/your_db_name
     frontend:
       build: ./frontend
       ports:
         - "3000:3000"
       depends_on:
         - backend
   ```

4. **Hot Reload Setup:**  The frontend likely uses a tool like `webpack` or `vite` which provides hot reloading.  Check the `frontend` directory for instructions (e.g., `npm run dev`).


### Option 2: Native Development

This option requires installing dependencies directly on your system.

1. **Backend Setup:**
   ```bash
   python3 -m venv .venv  # Create a virtual environment
   source .venv/bin/activate  # Activate the virtual environment
   pip install -r backend/requirements.txt  # Install backend dependencies
   ```

2. **Frontend Setup:**
   ```bash
   cd frontend
   npm install  # Install frontend dependencies
   ```

3. **Database Setup:** Install PostgreSQL locally.  Configure the database using the `psql` command-line tool or a GUI tool like pgAdmin. Create a database with the name specified in your environment variables (see below).


## Environment Configuration

**Required Environment Variables:**

* `DATABASE_URL`:  Connection string for your database (e.g., `postgres://user:password@host:port/database`).
* `STRIPE_SECRET_KEY`: Your Stripe secret key for payment processing.
* `STRIPE_PUBLISHABLE_KEY`: Your Stripe publishable key.
* `SECRET_KEY`: A secret key for your backend (for security).
* `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`:  Settings for sending emails (e.g., using SendGrid or similar).


**Local Development .env File Setup:**

Create a `.env` file in the root directory of the project and populate it with your local environment variables.  **Do not commit this file to version control.**  Example:

```
DATABASE_URL=postgres://your_user:your_password@localhost:5432/your_db_name
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
SECRET_KEY=a_very_secret_key
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
```


**Configuration for Different Environments:**

Use environment variables to manage settings for different environments (development, testing, production).  Consider using a configuration management tool like `python-dotenv` for Python and similar tools for JavaScript.


## Running the Application

**Start Commands for Development:**

* **Docker:** `docker-compose up -d`
* **Native:**
    * Start the backend server (e.g., `python manage.py runserver` if using Django).
    * Start the frontend development server (e.g., `npm run dev`).


**How to Access Frontend and Backend:**

* **Frontend:** Access the e-commerce platform through your web browser at `http://localhost:3000` (or the port specified in your `docker-compose.yml` or development server).
* **Backend API:** The API endpoints will be available at `http://localhost:8000/api/` (or the appropriate port).  You can use tools like Postman or curl to test the API.


**API Documentation Access:**  The project might include API documentation generated using tools like Swagger or OpenAPI. Check the project's documentation for details.


## Development Workflow

**Git Workflow and Branching Strategy:**  Use a Git branching strategy like Gitflow (feature branches, develop branch, master/main branch).

**Code Formatting and Linting Setup:**  Use tools like Prettier (JavaScript) and Black (Python) for code formatting and ESLint (JavaScript) and Pylint (Python) for linting. Configure your IDE to automatically format code on save.

**Testing Procedures:**  Write unit and integration tests.  Use a testing framework like pytest (Python) and Jest (JavaScript).

**Debugging Setup:**  Use your IDE's debugger or tools like pdb (Python) and the browser's developer tools for debugging.


## Database Management

**Running Migrations:**  Use database migration tools (e.g., Alembic for Python, migrations in your ORM).

**Seeding Development Data:** Create scripts to seed your database with initial data for development.

**Database Reset Procedures:**  Create scripts to easily reset your database to a clean state.


## Testing

**Running Unit Tests:**  Run unit tests using the appropriate test runner (e.g., `pytest` or `npm test`).

**Running Integration Tests:**  Run integration tests to test interactions between different components.

**Test Coverage Reports:**  Generate test coverage reports to track the percentage of code covered by tests.


## Common Development Tasks

**Adding New API Endpoints:**  Follow the project's API design guidelines.  Write unit and integration tests.

**Adding New Frontend Components:**  Use the project's component structure and styling guidelines.  Write unit tests for components.

**Database Schema Changes:**  Use database migrations to manage schema changes.  Update relevant models and tests.

**Adding Dependencies:**  Add dependencies using `pip` (Python) and `npm` (JavaScript). Update the relevant files (e.g., `requirements.txt`, `package.json`).


## Troubleshooting

**Common Setup Issues:**  Check for typos in environment variables, incorrect database configurations, and missing dependencies.

**Port Conflicts Resolution:** Change ports used by services if there are conflicts.

**Dependency Issues:**  Check for conflicting dependencies and resolve them using tools like `pip-tools` or `npm-check`.

**Environment Variable Problems:**  Make sure environment variables are correctly set and accessible to your application.


## Contributing

**Code Style Guidelines:** Adhere to the project's code style guidelines (e.g., PEP 8 for Python, Airbnb style guide for JavaScript).

**Pull Request Process:** Create clear and concise pull requests with descriptive titles and detailed explanations of changes.

**Issue Reporting:**  Report issues clearly and concisely, providing relevant information (error messages, steps to reproduce, expected behavior).


This guide provides a comprehensive starting point.  The specifics of commands and configurations may vary slightly depending on the project's exact technologies and structure. Always refer to the project's `README` file and other documentation for the most accurate and up-to-date information.

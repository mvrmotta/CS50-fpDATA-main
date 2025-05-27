# CS50 - Pet Finance 
#### Video Demo:  <(https://youtu.be/NhFBcfmcS7A)>
#### Description:



🐾 Pet Finance
Pet Finance is a comprehensive web application that allows users to manage and analyze their pet-related expenses effectively. This project was built using the Flask web framework and incorporates user authentication, database management, dynamic data visualization, and a clean, responsive user interface using Bootstrap.

This application serves pet owners who want to keep track of how much they are spending on their pets, categorized by types of expenses (e.g., food, veterinary care, toys). Additionally, it offers a dashboard with charts and summaries to help users make informed financial decisions related to their pets.



🚀 Project Overview
The core functionality of Pet Finance includes:

User Registration and Login: secure authentication system using Flask-Login and WTForms.

Pet Management: users can register multiple pets and keep track of each one’s specific expenses.

Expense Tracking: record and categorize expenses such as food, veterinary services, hygiene, transportation, toys, and more.

Dashboard: visual representation of spending through charts, total monthly expenses, and category-wise analysis.

Responsive Interface: built with Bootstrap for a modern and clean look, ensuring usability on both desktop and mobile devices.




📁 File and Directory Structure


/app.py
This is the main entry point of the application, responsible for initializing the Flask app, configuring database connections with SQLAlchemy, registering blueprints, and setting up Flask-Login for user authentication.



/models.py
Defines the SQLAlchemy models for the database:

User: represents the application’s users, including username and password hash.

Pet: linked to users, stores pet-specific data such as name, species, breed, birth date, and weight.

Category: pre-defined categories of expenses to ensure consistency in data analysis.

Expense: linked to both a pet and category, includes amount and date of the expense.



/routes/
Contains blueprint files that organize routes logically:

users.py: handles registration, login, logout, and user session management.

pets.py: CRUD operations for managing pets.

expenses.py: operations for adding, listing, and removing expenses.

dashboard.py: fetches data for analytics and serves the dashboard page.



/templates/
Jinja2 HTML templates for rendering the frontend:

base.html: layout template with navigation bar and footer.

home.html: landing page with project description and call to action.

login.html / register.html: user authentication forms.

add_pet.html / list_pets.html: pet management interfaces.

add_expense.html / list_expenses.html: expense management.

dashboard.html: displays user spending analytics with charts.



/static/
Contains static files such as images including icons and landing page graphics.



/forms/
Houses Flask-WTF form definitions for login, registration, adding pets, and adding expenses. This abstraction makes form validation and CSRF protection seamless.



/scripts/seed_categories.py
A simple script to seed the database with predefined categories of expenses to ensure consistency in data analysis. This was necessary to avoid data inconsistency caused by free-text category entries.



🧠 Design Decisions
Categorization
Initially, I debated whether to allow users to define their own categories of expenses. However, after consideration, I opted for pre-defined categories to ensure consistency in data analysis. Free-form categories could have led to inconsistent labels like "Vet", "Veterinary", or "Vet visit", making it harder to visualize and aggregate data effectively.


Database Choice
For simplicity and ease of deployment, I used SQLite during development. While SQLite suffices for small-scale use, I designed the ORM models to be easily portable to PostgreSQL, which would be more appropriate for production-level deployments.


Frontend Framework
I chose Bootstrap for styling due to its simplicity, responsiveness, and modern aesthetics. This ensured that the application is usable on both mobile and desktop devices without requiring extensive custom CSS.


Data Visualization
To provide an intuitive representation of user expenses, I implemented Chart.js for the dashboard. I initially experimented with pie charts but later switched to stacked bar charts for better temporal analysis of expenses by category over different months.


⚙️ Technologies Used
Flask – web framework.

Flask-SQLAlchemy – ORM for database models.

Flask-Migrate – for database migrations.

Flask-WTF – simplifies form handling with CSRF protection.

Flask-Login – user session and authentication management.

Bootstrap – frontend styling.

Chart.js – dynamic data visualization in the dashboard.

gunicorn – production-grade WSGI HTTP server.



💡 Future Enhancements
Add support for multiple currencies.

Allow users to set budget limits and receive alerts when exceeded.

Add email notifications for regular expense summaries.

Add alerts for upcoming events (e.g.: vaccination, renewal of anti-flea collar).

Add expense prediction for upcoming months based on data analysis.



✅ Conclusion
Pet Finance represents the culmination of my learning experience from the CS50 course, combining backend development, database modeling, frontend templating, and data visualization. The design decisions made throughout the development process reflect a balance between simplicity for the end-user and ensuring data integrity for meaningful analysis.

I am proud of this project as it showcases my growing skills in web development and data analysis and demonstrates my ability to bring an idea from conception to deployment.



🖥️ Deployment
The application is ready for deployment on platforms such as Render or Railway and includes configuration files like Procfile and requirements.txt to ensure smooth deployment.



📩 Contact
If you would like to connect or give feedback, feel free to reach out via:

GitHub: mvrmotta

LinkedIn: https://www.linkedin.com/in/marcosvmotta/
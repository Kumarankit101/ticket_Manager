# FastAPI Ticketing System

This project is a ticketing system built using FastAPI, SQLAlchemy, and Ably for real-time updates. It provides APIs for managing tickets and agents, with real-time notifications for ticket updates.

## Project Structure

- **app/**: Contains the main application code.

  - **main.py**: The entry point of the FastAPI application.
  - **models.py**: Defines the SQLAlchemy models for the database.
  - **database.py**: Handles database connections and session management.
  - **crud.py**: Contains CRUD operations for tickets and agents.
  - **schemas.py**: Defines Pydantic models for request and response validation.
  - **realtime.py**: Manages real-time updates using Ably.
  - **routers/**: Contains the API route definitions.
    - **tickets.py**: API routes for ticket management.
    - **agents.py**: API routes for agent management.

- **alembic/**: Contains database migration scripts.
- **.env**: Environment variables for configuration.
- **requirements.txt**: Python dependencies for the project.

## Features

- **Ticket Management**: Create, read, update, and delete tickets.
- **Agent Management**: Create and list agents.
- **Real-Time Updates**: Receive real-time notifications for ticket updates using Ably.
- **Database Migrations**: Manage database schema changes with Alembic.

## Setup

This project requires **Python 3.11.11**.

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   - Create a `.env` file in the root directory with the following variables:
     ```
     SUPABASE_URL=<your-supabase-url>
     SUPABASE_KEY=<your-supabase-key>
     DATABASE_URL=<your-database-url>
     ABLY_API_KEY=<your-ably-api-key>
     ```

5. **Run database migrations**:

   ```bash
   alembic upgrade head
   ```

6. **Start the FastAPI application**:

   ```bash
   uvicorn app.main:app --reload
   ```

7. **Access the API documentation**:
   - Open your browser and go to `http://localhost:8000/docs` to view the interactive API documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

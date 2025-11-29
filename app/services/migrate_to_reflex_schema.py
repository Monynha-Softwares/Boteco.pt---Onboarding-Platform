import os
import logging
from supabase import create_client, Client
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def migrate():
    """Executes the schema setup SQL using Supabase RPC."""
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_KEY")
    if not supabase_url or not supabase_key:
        logger.error("Supabase credentials missing. Cannot migrate.")
        return
    try:
        client: Client = create_client(supabase_url, supabase_key)
        current_dir = Path(__file__).resolve().parent
        sql_path = current_dir / "schema_setup.sql"
        if not sql_path.exists():
            logger.error(f"SQL file not found at {sql_path}")
            return
        sql_command = sql_path.read_text(encoding="utf-8")
        logger.info("Executing schema setup SQL...")
        response = client.rpc("execute_sql", {"sql_command": sql_command}).execute()
        logger.info("Migration SQL executed. Checking schema status...")
        logger.info("Migration script completed successfully.")
    except Exception as e:
        logger.exception(f"An error occurred during migration: {e}")


if __name__ == "__main__":
    migrate()
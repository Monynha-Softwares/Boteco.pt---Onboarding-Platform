import os
import logging
import psycopg
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def setup_schema():
    """
    Sets up the reflex schema using a direct database connection.
    Requires DATABASE_URL environment variable.
    """
    db_url = os.getenv("DATABASE_URL") or os.getenv("REFLEX_DB_URL")
    if not db_url:
        logger.error("DATABASE_URL or REFLEX_DB_URL environment variable is not set.")
        logger.error(
            "Please set it to your Supabase connection string (Transaction Pooler or Session Pooler)."
        )
        return
    if "+psycopg" in db_url:
        db_url = db_url.replace("postgresql+psycopg://", "postgresql://")
        logger.info("Adjusted connection string for psycopg3 compatibility.")
    current_dir = Path(__file__).resolve().parent
    sql_path = current_dir / "schema_setup.sql"
    if not sql_path.exists():
        logger.error(f"SQL file not found at {sql_path}")
        return
    try:
        sql_command = sql_path.read_text(encoding="utf-8")
        logger.info("Connecting to database...")
        with psycopg.connect(db_url) as conn:
            with conn.cursor() as cur:
                logger.info("Executing schema setup SQL...")
                cur.execute(sql_command)
            conn.commit()
        logger.info("✅ Schema setup completed successfully!")
        logger.info("=" * 60)
        logger.info("CRITICAL NEXT STEP:")
        logger.info("Go to Supabase Dashboard > Settings > API")
        logger.info("Add 'reflex' to the 'Exposed schemas' list")
        logger.info("Save the changes to allow API access to your new tables.")
        logger.info("=" * 60)
    except Exception as e:
        logger.exception(f"An error occurred during schema setup: {e}")


if __name__ == "__main__":
    setup_schema()
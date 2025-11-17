from fastapi import FastAPI, Request, Response
from supabase import create_client, Client
import os
import logging

api_app = FastAPI()


@api_app.post("/api/provision_org")
async def provision_org_route(request: Request) -> Response:
    """API endpoint to provision a new organization schema in Supabase."""
    try:
        body = await request.json()
        boteco_username = body.get("boteco_username")
        if not boteco_username or not boteco_username.strip():
            return Response(
                content='{"error": "boteco_username is required"}',
                status_code=400,
                media_type="application/json",
            )
        if not boteco_username.isalnum() and "_" not in boteco_username:
            return Response(
                content='{"error": "Invalid boteco_username format"}',
                status_code=400,
                media_type="application/json",
            )
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY", os.getenv("SUPABASE_KEY"))
        if not supabase_url or not supabase_key:
            logging.error("Supabase URL or Key not configured for provisioning.")
            return Response(
                content='{"error": "Server configuration error"}',
                status_code=500,
                media_type="application/json",
            )
        schema_name = f"org_{boteco_username}"
        sql_command = f'CREATE SCHEMA IF NOT EXISTS "{schema_name}";'
        supabase_admin: Client = create_client(supabase_url, supabase_key)
        response = await supabase_admin.rpc(
            "execute_sql", {"sql_command": sql_command}
        ).execute()
        if response.error:
            raise Exception(f"Supabase RPC error: {response.error.message}")
        logging.info(f"Successfully provisioned schema: {schema_name}")
        return Response(
            content=f'{{"message": "Schema {schema_name} provisioned successfully"}}',
            status_code=200,
            media_type="application/json",
        )
    except Exception as e:
        logging.exception(f"Error provisioning organization: {e}")
        return Response(
            content=f'{{"error": "Failed to provision schema: {str(e)}"}}',
            status_code=500,
            media_type="application/json",
        )
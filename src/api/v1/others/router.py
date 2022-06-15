# coding: utf-8
from fastapi import APIRouter
from starlette.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    # get_swagger_ui_oauth2_redirect_html,
)
from main import settings, app
from ..dependencies import app_token

router = APIRouter()


@router.get("/schema.json", include_in_schema=False, dependencies=[app_token])
async def get_open_api_endpoint_gateway():
    schema = get_openapi(
        title=settings.project_title,
        version=settings.project_version,
        routes=app.routes
    )
    return JSONResponse(schema)


@router.get("/docs", include_in_schema=False, dependencies=[app_token])
async def custom_swagger_ui_html():
    response = get_swagger_ui_html(
        openapi_url='/schema.json',
        title="Swagger UI",
        # oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/swagger-static/swagger-ui-bundle.js",
        swagger_css_url="/swagger-static/swagger-ui.css",
    )
    response.set_cookie(
        key='token',
        value=settings.api_token,
        httponly=True,
        max_age=1800,
        expires=1800,
    )    
    return response

# @router.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
# async def swagger_ui_redirect():
#     return get_swagger_ui_oauth2_redirect_html()


@router.get("/redoc", include_in_schema=False, dependencies=[app_token])
async def redoc_html():
    response = get_redoc_html(
        openapi_url='/schema.json',
        title="ReDoc",
        redoc_js_url="/swagger-static/redoc.standalone.js",
    )
    response.set_cookie(
        key='token',
        value=settings.api_token,
        httponly=True,
        max_age=1800,
        expires=1800,
    )    
    return response


@router.get("/api/status", status_code=200)
async def status():
    return JSONResponse({'status': 'Ok'})

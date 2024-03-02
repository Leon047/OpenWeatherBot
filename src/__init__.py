"""
__init__.py - Module for initializing the router and including view routers.
"""

from aiogram import Router
from .views import router as main_router

__all__ = ("router",)

# Initializing the main router
router = Router(name=__name__)

# Include the main_router to the router
router.include_router(main_router)

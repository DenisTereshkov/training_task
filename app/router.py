from typing import Annotated
from collections import OrderedDict

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError

from .repository import UrlRepository
from .schemas import UrlCreate

router = APIRouter(tags=['Urls'])


@router.post('/', status_code=status.HTTP_201_CREATED)
async def add_url(
    url: Annotated[UrlCreate, Depends()],
):
    """
    Adds a new URL to the database.
    """
    try:
        shorten_url = await UrlRepository.add_url(url)
        response = OrderedDict()
        response['id'] = shorten_url.id
        response['url'] = shorten_url.url
        response['abbreviated_url'] = shorten_url.abbreviated_url
        return response
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="not unique URL."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get(
        '/{shorten_url_id}',
        status_code=status.HTTP_307_TEMPORARY_REDIRECT
    )
async def get_url(shorten_url_id: int):
    """
    Retrieves the original URL associated with a shortened URL ID.
    """
    try:
        url = await UrlRepository.get_url(shorten_url_id)
        if url is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="URL not found"
            )
        return {'url': url.url}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

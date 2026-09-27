# subhashkumar_module3_4.py

# make python pagaination  /items?page=2&size=5 return page metadata. 
# Why pagination?      

from fastapi import FastAPI

# Create the FastAPI application.
app = FastAPI()


# Create some sample items.
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
    {"id": 4, "name": "Item 4"},
    {"id": 5, "name": "Item 5"},
    {"id": 6, "name": "Item 6"},
    {"id": 7, "name": "Item 7"},
    {"id": 8, "name": "Item 8"},
    {"id": 9, "name": "Item 9"},
    {"id": 10, "name": "Item 10"},
    {"id": 11, "name": "Item 11"},
    {"id": 12, "name": "Item 12"},
    {"id": 13, "name": "Item 13"},
    {"id": 14, "name": "Item 14"},
    {"id": 15, "name": "Item 15"},
]


@app.get("/items")
def get_items(page: int = 1, size: int = 5):
    """Return items for the requested page with pagination metadata."""

    # Calculate the starting position.
    start = (page - 1) * size

    # Calculate the ending position.
    end = start + size

    # Get only the items required for this page.
    page_items = items[start:end]

    # Calculate the total number of items.
    total_items = len(items)

    # Calculate the total number of pages.
    total_pages = (total_items + size - 1) // size

    # Return items and pagination metadata.
    return {
        "items": page_items,
        "paging_info": {
            "page": page,
            "size": size,
            "total_items": total_items,
            "total_pages": total_pages,
            "has_previous": page > 1,
            "has_next": page < total_pages
        }
    }

'''
Why do we need pagination?

Imagine a database contains 1 million items.

Without pagination: 
    An API request will give you complete data as response
This can cause:
    Large response size
    More network traffic
    Higher memory usage
    Slower API response
    Slower frontend rendering
    More database processing

With pagination:
    API request will provide only limited data based on paging parameters

So pagination allows the client to retrieve data in small, manageable pages.
Pagination parameters:
    page = which page you want
    size = how many records per page
    total_items = total records available
    total_pages = number of pages available
    has_previous = whether a previous page exists
    has_next = whether a next page exists
'''
# Start the server
# python -m uvicorn subhashkumar_module3_6:app --reload
# http://127.0.0.1:8000/items?page=2&size=5


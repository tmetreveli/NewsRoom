from ninja import NinjaAPI
from ninja import NinjaAPI, Schema, Query
from typing import List
from content.models import Article, Category
from modules.models import Menu, Block
from typing import Optional
from django.shortcuts import get_object_or_404
from datetime import datetime


api = NinjaAPI()


class ArticleSchema(Schema):
    id: int
    title: str
    description: str
    publication_datetime: datetime = None
    author_id: int
    category_id: int
    tags: List[int]
    main_image: str
    publishing: bool


class BlockSchema(Schema):
    id: int
    article_id: int
    visual_selection: str
    block_position: str
    block_row: int
    title: str
    show_title: bool


class MenuSchema(Schema):
    id: int
    name: str
    link: str
    is_external: bool
    category_id: Optional[int] = None
    is_active: bool


class CategorySchema(Schema):
    id: int
    name: str
    logo: str
    parent_id: Optional[int] = None


# @api.get("/articles", response=List[ArticleSchema])
# def list_articles(request):
#     # if category:
#     #     queryset = queryset.filter(category=category)
#     # if tag:
#     #     queryset = queryset.filter(tags__contains=[tag])
#     return Article.objects.all()
    
@api.get("/articles", response=List[ArticleSchema])
def list_articles(request, category: str = None, tag: str = None, skip: int = 0, limit: int = 10):
    queryset = Article.objects.all()
    if category:
        queryset = queryset.filter(category=category)
    if tag:
        print(tag)
        queryset = queryset.filter(tags__name=tag)
        print(queryset)

    articles = []
    for article in queryset[skip: skip + limit]:
        tag_ids = list(article.tags.values_list('id', flat=True))  
        article_data = {
            "id": article.id,
            "title": article.title,
            "description": article.description,
            "publication_datetime": article.publication_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "author_id": article.author_id,
            "category_id": article.category_id,
            "tags": tag_ids,  
            "main_image": article.main_image.url if article.main_image else None,
            "publishing": article.publishing
        }
        articles.append(article_data)

    return articles



@api.get("/blocks", response=List[BlockSchema])
def list_blocks(request):
    return Block.objects.all()


@api.get("/menus", response=List[MenuSchema])
def list_menus(request):
    return Menu.objects.all()


@api.get("/categories", response=List[CategorySchema])
def list_categories(request):
    return Category.objects.all()

@api.post("/articles", response=ArticleSchema)
def create_article(request, payload: ArticleSchema):
    article = Article.objects.create(**payload.dict())
    return article


@api.post("/blocks", response=BlockSchema)
def create_block(request, payload: BlockSchema):
    block = Block.objects.create(**payload.dict())
    return block


@api.post("/menus", response=MenuSchema)
def create_menu(request, payload: MenuSchema):
    menu = Menu.objects.create(**payload.dict())
    return menu


@api.post("/categories", response=CategorySchema)
def create_category(request, payload: CategorySchema):
    category = Category.objects.create(**payload.dict())
    return category

@api.put("/articles/{article_id}", response=ArticleSchema)
def update_article(request, article_id: int, payload: ArticleSchema):
    article = get_object_or_404(Article, id=article_id)
    for attr, value in payload.dict().items():
        setattr(article, attr, value)
    article.save()
    return article

@api.put("/blocks/{block_id}", response=BlockSchema)
def update_block(request, block_id: int, payload: BlockSchema):
    block = get_object_or_404(Block, id=block_id)
    for attr, value in payload.dict().items():
        setattr(block, attr, value)
    block.save()
    return block


@api.put("/menus/{menu_id}", response=MenuSchema)
def update_menu(request, menu_id: int, payload: MenuSchema):
    menu = get_object_or_404(Menu, id=menu_id)
    for attr, value in payload.dict().items():
        setattr(menu, attr, value)
    menu.save()
    return menu


@api.put("/categories/{category_id}", response=CategorySchema)
def update_category(request, category_id: int, payload: CategorySchema):
    category = get_object_or_404(Category, id=category_id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return category

# DELETE operations
@api.delete("/articles/{article_id}")
def delete_article(request, article_id: int):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return {"success": True}


@api.delete("/blocks/{block_id}")
def delete_block(request, block_id: int):
    block = get_object_or_404(Block, id=block_id)
    block.delete()
    return {"success": True}


@api.delete("/menus/{menu_id}")
def delete_menu(request, menu_id: int):
    menu = get_object_or_404(Menu, id=menu_id)
    menu.delete()
    return {"success": True}


@api.delete("/categories/{category_id}")
def delete_category(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return {"success": True}
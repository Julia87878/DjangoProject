from .models import Product


class ProductService:

    @staticmethod
    def get_products_list_by_category(category_id):
        """Метод, который получает список продуктов по указанной категории."""
        category_products = Product.objects.filter(category_id=category_id)

        if not category_products.exists():
            return None
        return category_products

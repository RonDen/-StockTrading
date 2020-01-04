from .models import StockInfo


def get_top10():
    return StockInfo.objects.all().order_by('-change_extent')[:10]






from django import template
from django.utils.safestring import mark_safe

register = template.Library()

TABLE_HEAD = """
            <table class="table">
              <tbody>
            """

TABLE_TAIL = """
                </tbody>
            </table>  
            """

TABLE_CONTENT = """
                <tr>
                    <td>{name}</td>
                    <td>{value}</td>
                </tr>
                """

PRODUCT_SPEC = {
    'notebook': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Частота процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видеокарта': 'video',
        'Время работы аккумулятора': 'time_without_charge',
    },
    'smartphone': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display_type',
        'Разрешение': 'resolution',
        'Оперативная память': 'ram',
        'Объём батареи': 'accum_volume',
        'Наличие карты памяти': 'sd',
        'Объём карты памяти': 'sd_volume_max',
        'Основная камера (МП)': 'main_cam_mp',
        'Фронтальная камера (МП)': 'frontal_cam_mp',
    },
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    table_content = get_product_spec(product, model_name)
    return mark_safe(TABLE_HEAD + table_content + TABLE_TAIL)

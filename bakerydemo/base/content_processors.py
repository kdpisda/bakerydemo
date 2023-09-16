from bakerydemo.base.models import FooterSettings


def footer_context(request):
    footer_settings = FooterSettings.objects.first()  # Replace with your actual retrieval logic
    total_columns = len(footer_settings.columns) if footer_settings and footer_settings.columns else 0

    if total_columns == 1:
        col_sizes = {'xs': 12, 'sm': 12, 'md': 12, 'lg': 12}
    elif total_columns == 2:
        col_sizes = {'xs': 12, 'sm': 12, 'md': 6, 'lg': 6}
    elif total_columns == 3:
        col_sizes = {'xs': 12, 'sm': 12, 'md': 4, 'lg': 4}
    elif total_columns == 4:
        col_sizes = {'xs': 12, 'sm': 12, 'md': 3, 'lg': 3}
    else:
        col_sizes = {'xs': 12, 'sm': 12, 'md': 3, 'lg': 3}

    return {'total_columns': total_columns, 'col_sizes': col_sizes}

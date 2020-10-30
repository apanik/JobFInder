from p7.settings_dev import APP_VERSION_NUMBER


def footer_context(request):
    return {'APP_VERSION_NUMBER': APP_VERSION_NUMBER}
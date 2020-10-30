from django.views.generic import TemplateView

from p7.views import get_header_footer


class ProfessionalMessagesView(TemplateView):
    template_name = "professional_messages.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class CompanyMessagesView(TemplateView):
    template_name = "company_messages.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class ProfessionalNotificationView(TemplateView):
    template_name = "professional_notification.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)


class CompanyNotificationView(TemplateView):
    template_name = "company_notification.html"

    def get(self, request, *args, **kwargs):
        header, footer = get_header_footer(request)
        return super().get(request, *args, **kwargs, header=header, footer=footer)

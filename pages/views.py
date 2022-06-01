from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Project, Faq, Term, SalesOffice, Country, LocalStore, Distributor


class DistributorsView(TemplateView):
    template_name = "pages/distributors.html"

    def get_context_data(self, **kwargs):
        context = super(DistributorsView, self).get_context_data(**kwargs)
        distributors = Distributor.objects.all()
        context['page'] = 'Distributors'
        context['distributors'] = distributors
        return context


class OurStoresView(TemplateView):
    template_name = "pages/our_stores.html"

    def get_context_data(self, **kwargs):
        context = super(OurStoresView, self).get_context_data(**kwargs)
        stores = LocalStore.objects.all()
        context['page'] = 'Our Stores'
        context['stores'] = stores
        return context


class SalesOfficesView(TemplateView):
    template_name = "pages/sales_offices.html"

    def get_context_data(self, **kwargs):
        context = super(SalesOfficesView, self).get_context_data(**kwargs)
        offices = SalesOffice.objects.all()
        context['page'] = 'Sales Offices'
        context['offices'] = offices
        return context


class FaqsView(TemplateView):
    template_name = "pages/faqs.html"

    def get_context_data(self, **kwargs):
        context = super(FaqsView, self).get_context_data(**kwargs)
        faqs = Faq.objects.all()
        context['page'] = 'FAQs'
        context['faqs'] = faqs
        return context


class TermsConditionsView(TemplateView):
    template_name = "pages/terms_conditions.html"

    def get_context_data(self, **kwargs):
        context = super(TermsConditionsView, self).get_context_data(**kwargs)
        terms = Term.objects.all()
        context['page'] = 'Terms and Conditions'
        context['terms'] = terms
        return context


class HistoryView(TemplateView):
    template_name = "pages/history.html"

    def get_context_data(self, **kwargs):
        context = super(HistoryView, self).get_context_data(**kwargs)
        context['page'] = 'History'
        return context


class ProjectsView(TemplateView):
    template_name = "pages/projects.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data(**kwargs)
        projects = Project.objects.all()
        context['page'] = 'Our Projects'
        context['projects'] = projects
        return context


def project_details(request, slug):
    project = Project.objects.get(slug=slug)
    page = project.name
    project_images = project.images()
    context = {
        'page': page,
        'project': project,
        'project_images': project_images,
    }
    return render(request, 'pages/project_details.html', context)


class RoomConceptsView(TemplateView):
    template_name = "pages/room_concepts.html"
    extra_context = {'page': 'Room Concepts'}


class SafetyCertificateView(TemplateView):
    template_name = "pages/safety_cetificates.html"
    extra_context = {'page': 'Safety Cetificates'}


class SizeGuideView(TemplateView):
    template_name = "pages/size_guide.html"
    extra_context = {'page': 'Size Guide'}


class TimeLineView(TemplateView):
    template_name = "pages/timeline.html"
    extra_context = {'page': 'Timeline'}


class DevelopmentMilestoneView(TemplateView):
    template_name = "pages/development_milestone.html"
    extra_context = {'page': 'Development Milestone'}


class VisionMissionView(TemplateView):
    template_name = "pages/vision_mission.html"
    extra_context = {'page': 'Vision and Mission'}


class WorldWideView(TemplateView):
    template_name = "pages/world_wide.html"
    extra_context = {'page': 'World Wide'}

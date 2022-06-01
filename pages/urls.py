from django.urls import path
from . import views
from .views import (DistributorsView, OurStoresView, SalesOfficesView, FaqsView, TermsConditionsView, HistoryView,
                    ProjectsView, RoomConceptsView, SafetyCertificateView, SizeGuideView, TimeLineView,
                    VisionMissionView, DevelopmentMilestoneView, WorldWideView, project_details)

urlpatterns = [
    path('distributors', DistributorsView.as_view(), name='distributors'),
    path('our-stores', OurStoresView.as_view(), name='our_stores'),
    path('sales-offices', SalesOfficesView.as_view(), name='sales_offices'),
    path('faqs', FaqsView.as_view(), name='faqs'),
    path('terms-conditions', TermsConditionsView.as_view(), name='terms_conditions'),
    path('history', HistoryView.as_view(), name='history'),
    path('room-concepts', RoomConceptsView.as_view(), name='room_concepts'),
    path('safety-cetificates', SafetyCertificateView.as_view(), name='safety_cetificates'),
    path('size-guide', SizeGuideView.as_view(), name='size_guide'),
    path('timeline', TimeLineView.as_view(), name='timeline'),
    path('vision-mission', VisionMissionView.as_view(), name='vision_mission'),
    path('development_milestone', DevelopmentMilestoneView.as_view(), name='development_milestone'),
    path('world-wide', WorldWideView.as_view(), name='world_wide'),
    path('projects', ProjectsView.as_view(), name='projects'),
    path('project/<slug:slug>', views.project_details, name='project_details'),
]

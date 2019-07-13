from django.urls import path, include

urlpatterns = [
    path(
        'users/', 
        include(
            ('api.user.urls', 'user'), 
            namespace='user'
        ),
    ),
    path(
        'mentors/', 
        include(
            ('api.mentor.urls', 'mentor'),
            namespace='mentor'
        ),
    ),
]

from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns('',
                        host(r'www', settings.ROOT_URLCONF, name='student'),
                        host(r'teacher', settings.TEACHER_URLCONF, name='teacher'),
                        host(r'admin', settings.ADMIN_URLCONF, name='admin'))

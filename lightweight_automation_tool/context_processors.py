from django.core.handlers.wsgi import WSGIRequest

from lightweight_automation_tool.constants import ACTIVE_TAB_ANCHOR_CLASS, ACTIVE_TAB_SVG_CLASS, INACTIVE_TAB_SVG_CLASS, \
    INACTIVE_TAB_ANCHOR_CLASS


def message_processor(request: WSGIRequest):
    is_index_path = request.path == '/'
    is_jenkins_path = request.path == '/jenkins/'
    return {
        'home_tab_anchor_class': ACTIVE_TAB_ANCHOR_CLASS if is_index_path else INACTIVE_TAB_ANCHOR_CLASS,
        'home_tab_svg_class': ACTIVE_TAB_SVG_CLASS if is_index_path else INACTIVE_TAB_SVG_CLASS,
        'jenkins_tab_anchor_class': ACTIVE_TAB_ANCHOR_CLASS if is_jenkins_path else INACTIVE_TAB_ANCHOR_CLASS,
        'jenkins_tab_svg_class': ACTIVE_TAB_SVG_CLASS if is_jenkins_path else INACTIVE_TAB_SVG_CLASS,
    }

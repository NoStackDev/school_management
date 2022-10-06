from django import template

register = template.Library()

@register.filter 
def unique(array, obj_key=None):
    result = []
    seen = []

    if (obj_key):
        for ele in array:
            if getattr(ele, obj_key) not in seen:
                seen.append(getattr(ele, obj_key))
                result.append(ele)
        return result

    for ele in array:
        if ele not in result:
            result.append(ele)
    return result


@register.filter
def student_assessments_filter(query_obj, subject_id):
    assessments = query_obj.studentassessment_set.filter(subject=subject_id)
    return assessments

@register.filter
def order_assessments(query_obj, assessment_dict):
    assessments_ordered = []
    for key, value in assessment_dict.items():
        assessments = query_obj.studentassessment_set.filter(assessment_type=key)
        assessments_ordered = assessments_ordered + [*assessments]
    return assessments_ordered

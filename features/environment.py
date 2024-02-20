def before_all(context):
    # Here we can initiate or launch something if would be necessary
    print("before all scenarios do somthing")


def before_scenario(context, scenario):
    # Here we can initiate or launch something if would be necessary
    print("before scenario do somthing")


def after_scenario(context, scenario):
    # Here we can initiate or launch something if would be necessary
    print("after scenario do somthing")


def after_all(context):
    # Here we can initiate or launch something if would be necessary
    print("after all scenarios do somthing")

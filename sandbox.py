# Placeholder: production should run heavy symbolic work in sandboxed worker/container
def run_in_sandbox(callable_fn, *args, **kwargs):
    return callable_fn(*args, **kwargs)

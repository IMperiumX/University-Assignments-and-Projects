# Reverse

edirect(to, *args, permanent=False, **kwargs)¶

    Returns an HttpResponseRedirect to the appropriate URL for the arguments passed.

    The arguments could be:

        A model: the model’s get_absolute_url() function will be called.
        A view name, possibly with arguments: reverse() will be used to reverse-resolve the name.
        An absolute or relative URL, which will be used as-is for the redirect location.

    By default issues a temporary redirect; pass permanent=True to issue a permanent redirect.
# AUTOGENERATED! DO NOT EDIT! File to edit: build_lib.ipynb (unless otherwise specified).

__all__ = ['GH_OPENAPI_URL', 'GH_DOC_URL', 'build_funcs']

# Cell
from fastcore.utils import *
from fastcore.foundation import *
import pprint

# Cell
#export
GH_OPENAPI_URL = 'https://github.com/github/rest-api-description/raw/main/descriptions/api.github.com/api.github.com.json?raw=true'
GH_DOC_URL = 'https://docs.github.com/'


# Cell
def build_funcs(pre,
                nm='ghapi/metadata.py',
                url=GH_OPENAPI_URL,
                docurl=GH_DOC_URL):
    """Build module funcs.py from an Open API spec and optionally filter by a path `pre`"""
    def _get_detls(o):
        data = nested_idx(o, *'requestBody content application/json schema properties'.split()) or {}
        url = o['externalDocs']['url'][len(docurl):]
        return (o['operationId'], o['summary'], url, list(data.keys()))

    js = urljson(url)
    paths = {o[len(pre):]:v for o,v in js['paths'].items() if o.startswith(pre)}
    _funcs = [(path, verb) + _get_detls(detls)
              for path,verbs in paths.items() for verb,detls in verbs.items()]
    Path(nm).write_text("funcs = " + pprint.pformat(_funcs, width=360))
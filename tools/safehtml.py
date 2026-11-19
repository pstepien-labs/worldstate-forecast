"""Markup check for published HTML (framework 1.9, WP-17). Python standard library only.

Agent-written HTML (the brief body) and generated pages are published on GitHub Pages. Text from the
web reaches them through the agents, so before publishing we refuse active content and links to
hosts we must never link: scripts, frames, event-handler attributes, javascript: URLs, and links to
forbidden or no-republish domains (CLAUDE.md rules 3.9 and 6).
"""
import os
import re
from urllib.parse import urlparse

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ACTIVE_TAGS = re.compile(r'<\s*(script|iframe|object|embed|form|base|meta\s+http-equiv)\b', re.I)
EVENT_ATTR = re.compile(r'<[^>]*\s(on[a-z]+)\s*=', re.I)
JS_URL = re.compile(r'(?:href|src|action|formaction)\s*=\s*["\']?\s*(?:javascript|vbscript|data):', re.I)
URL_ATTR = re.compile(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']', re.I)


def _domains(name):
    out = set()
    try:
        with open(os.path.join(ROOT, 'sources', 'harvest', name), encoding='utf-8') as f:
            for line in f:
                line = line.split('#', 1)[0].strip().lower()
                if line and '.' in line and ' ' not in line:
                    out.add(line.lstrip('*.'))
    except OSError:
        pass
    return out


def blocked_hosts():
    return _domains('forbidden_domains.txt') | _domains('no_republish.txt')


def problems(page, allowed_hosts=None, allow_scripts=()):
    """List of problems; empty = safe to publish.
    allowed_hosts: if given, every absolute link must point to one of these hosts (or a subdomain).
    allow_scripts: exact <script>…</script> blocks that belong to our own template and are accepted."""
    for block in allow_scripts:
        page = page.replace(block, '')
    found = []
    for m in ACTIVE_TAGS.finditer(page):
        found.append(f'active element <{m.group(1)}>')
    for m in EVENT_ATTR.finditer(page):
        found.append(f'event-handler attribute {m.group(1)}=')
    if JS_URL.search(page):
        found.append('javascript:/data: URL')
    blocked = blocked_hosts()
    for m in URL_ATTR.finditer(page):
        host = (urlparse(m.group(1)).hostname or '').lower()
        if not host:
            continue
        if any(host == b or host.endswith('.' + b) for b in blocked):
            found.append(f'link to a blocked host: {host}')
        elif allowed_hosts is not None and not any(host == a or host.endswith('.' + a) for a in allowed_hosts):
            found.append(f'link to a host outside the allow list: {host}')
    return sorted(set(found))

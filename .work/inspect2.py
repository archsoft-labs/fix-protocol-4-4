import json

out = js("""
(() => {
  const c = document.querySelector('section.fix-dictionary .col-12');
  if (!c) return 'no section';
  return c.innerHTML.slice(0, 6000);
})()
""")
print(out)

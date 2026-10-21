(function(){
  var c = window.CMC_CONFIG || {};
  document.querySelectorAll('[data-phone]').forEach(function(a){
    a.href = (a.getAttribute('data-phone') === 'sms' ? 'sms:' : 'tel:') + c.PHONE_E164;
  });
  document.querySelectorAll('[data-phone-text]').forEach(function(e){ e.textContent = c.PHONE_DISPLAY; });
  var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();

  // Microsoft Bookings embed (only for a real https URL)
  var url = (c.BOOKINGS_URL || '').trim(), emb = document.getElementById('book-embed'), fb = document.getElementById('book-fallback');
  if (emb && /^https:\/\//i.test(url)) {
    var f = document.createElement('iframe');
    f.src = url; f.title = 'Book an appointment with Curo My Car (Microsoft Bookings)';
    f.loading = 'lazy'; f.setAttribute('allowfullscreen', '');
    emb.appendChild(f); emb.hidden = false; if (fb) fb.hidden = true;
  }

  // Mobile nav
  var t = document.querySelector('.nav-toggle'), n = document.getElementById('nav');
  if (t && n) {
    t.addEventListener('click', function(){ var o = n.classList.toggle('open'); t.setAttribute('aria-expanded', o); });
    n.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', function(){ n.classList.remove('open'); t.setAttribute('aria-expanded', false); }); });
  }

  // Reveal on scroll
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} }); }, {rootMargin:'0px 0px -60px 0px'});
    document.querySelectorAll('.card,.steps li,.why > *,.book-fallback,.book-frame,form').forEach(function(el){ el.classList.add('reveal'); io.observe(el); });
  }

  // Quote form -> mailto
  var q = document.getElementById('quote-form');
  if (q) q.addEventListener('submit', function(e){
    e.preventDefault();
    if (!q.reportValidity()) return;
    var d = new FormData(q), L = [['Name','name'],['Phone','phone'],['Vehicle (year/make/model)','vehicle'],['Issue','issue'],['Location','location'],['Preferred time','time']];
    var body = L.map(function(x){ return x[0] + ': ' + (d.get(x[1]) || ''); }).join('\n');
    var subj = 'Quote request: ' + (d.get('vehicle') || 'vehicle') + ' (' + (d.get('name') || '') + ')';
    window.location.href = 'mailto:' + c.EMAIL + '?subject=' + encodeURIComponent(subj) + '&body=' + encodeURIComponent(body);
  });
})();

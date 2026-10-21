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

  // Quote form -> FormSubmit (AJAX)
  var q = document.getElementById('quote-form');
  if (q) {
    var st = document.getElementById('quote-status'), btn = q.querySelector('button[type="submit"]'), label = btn ? btn.innerHTML : '';
    var tel = 'tel:' + (c.PHONE_E164 || '+12817898609'), sms = 'sms:' + (c.PHONE_E164 || '+12817898609'), pd = c.PHONE_DISPLAY || '(281) 789-8609';
    var show = function(cls, html){ if (!st) return; st.className = 'form-status ' + cls; st.innerHTML = html; st.hidden = false; st.focus(); };
    q.addEventListener('submit', function(e){
      e.preventDefault();
      if (!q.reportValidity()) return;
      if (btn && btn.getAttribute('aria-busy') === 'true') return;
      var d = new FormData(q);
      if ((d.get('_honey') || '').trim()) return; // bot
      var payload = {
        name: d.get('name') || '', phone: d.get('phone') || '', vehicle: d.get('vehicle') || '', issue: d.get('issue') || '',
        location: d.get('location') || '', 'preferred time': d.get('time') || '',
        _subject: 'New quote request - curomycar.com', _template: 'table', _captcha: 'false', _honey: ''
      };
      if (btn) { btn.disabled = true; btn.setAttribute('aria-busy', 'true'); btn.innerHTML = '<span class="spin" aria-hidden="true"></span> Sending\u2026'; }
      if (st) st.hidden = true;
      fetch('https://formsubmit.co/ajax/' + (c.EMAIL || 'walter@curomycar.com'), {
        method: 'POST', headers: {'Content-Type': 'application/json', 'Accept': 'application/json'}, body: JSON.stringify(payload)
      }).then(function(r){ return r.json().catch(function(){ return {}; }).then(function(j){
        if (!r.ok || String(j.success) === 'false') throw new Error(j.message || ('HTTP ' + r.status));
      }); }).then(function(){
        q.reset();
        show('ok', 'Thanks! Walter will call or text you shortly.');
      }).catch(function(){
        show('err', 'Sorry, your request didn\u2019t go through. Please call or text Walter at ' + pd + '.' +
          '<span class="actions"><a class="btn btn-sm" href="' + tel + '">Call ' + pd + '</a><a class="btn btn-sm btn-ghost" href="' + sms + '">Text Walter</a></span>');
      }).then(function(){
        if (btn) { btn.disabled = false; btn.removeAttribute('aria-busy'); btn.innerHTML = label; }
      });
    });
  }
})();

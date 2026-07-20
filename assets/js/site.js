(() => {
  const sections = document.querySelectorAll('section.block, section.group, .hero, .page-hero');
  if (!sections.length) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) entry.target.classList.add('in');
    });
  }, { threshold: 0.12 });

  sections.forEach((section) => {
    section.classList.add('reveal');
    io.observe(section);
  });
})();

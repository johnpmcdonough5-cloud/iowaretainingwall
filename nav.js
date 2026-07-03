document.addEventListener('DOMContentLoaded', () => {
  const triggers = document.querySelectorAll('.nav-group-trigger, .flyout-trigger');

  triggers.forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      // Prevent default behavior
      e.preventDefault();
      
      const parent = trigger.parentElement;
      const isOpen = parent.hasAttribute('data-open');
      
      // Close sibling dropdowns at the same level
      const siblings = parent.parentElement.querySelectorAll(':scope > [data-open]');
      siblings.forEach(s => s.removeAttribute('data-open'));
      
      // If it wasn't open, open it
      if (!isOpen) {
        parent.setAttribute('data-open', 'true');
      }
    });
  });

  // Close all dropdowns when clicking outside of the navigation groups
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav-group') && !e.target.closest('.flyout-item')) {
      document.querySelectorAll('[data-open]').forEach(el => {
        el.removeAttribute('data-open');
      });
    }
  });
});

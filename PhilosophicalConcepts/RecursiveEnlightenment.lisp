(defun enlightenment (path)
  (if (null path)
      '("Enlightenment begins where the path ends.")
      (cons 'continue (enlightenment (cdr path)))))

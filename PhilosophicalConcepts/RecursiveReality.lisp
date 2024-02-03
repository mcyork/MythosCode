(defun reality (layers)
  (if (equal layers 0)
      '(this is the base reality)
      (cons 'layer (reality (- layers 1)))))

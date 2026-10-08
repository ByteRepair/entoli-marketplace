# Examples

Calibration samples: the diff, and the review comments Code Review should
produce for it.

## Diff

```diff
-    user := db.GetUser(id)
-    logger.Info("user login", "user", user)
+    user, _ := db.GetUser(ctx, id)
+    logger.Info("user login", "user", user.Name)
```

## Expected review comments

bug: `GetUser`'s error is discarded with `_`. A failed lookup logs a login for
the zero value and continues. Handle the error and return early. Example:
`if err != nil { return err }`.

security: `user.Name` is logged on every login attempt, including failures.
Logging an identifier such as the user ID avoids leaking personal data into
log aggregation systems that index the request log.

question: If `GetUser` now takes a context, are the other `db.Get*` call
sites in this file also meant to migrate in this change, or is that a
follow-up?

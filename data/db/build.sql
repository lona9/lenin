CREATE TABLE IF NOT EXISTS reminders (
  ReminderID NUMERIC PRIMARY KEY,
  ReminderTime DATE,
  ReminderText VARCHAR,
  ReminderAuthor VARCHAR,
  ReminderChannel NUMERIC
);

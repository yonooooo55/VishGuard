gcloud builds submit --tag gcr.io/vishguard/<AppName>  --project=<ProjectName>

gcloud run deploy --image gcr.io/vishguard/<AppName> --platform managed  --project=<ProjectName> --allow-unauthenticated
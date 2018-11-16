package com.example.bb.picassoapp;

import android.content.Context;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ImageView;

import com.squareup.picasso.Picasso;

import java.io.File;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Picasso.with(getApplicationContext()).setLoggingEnabled(true);

        Context ctx = getApplicationContext();

        ImageView imageView1 = (ImageView) findViewById(R.id.img1);
        ImageView imageView2 = (ImageView) findViewById(R.id.img2);

        Picasso
                .with(ctx)
                .load("https://www.dike.lib.ia.us/images/sample-1.jpg/image")
                .into(imageView1);

        Picasso.with(ctx).load(R.drawable.img).into(imageView2);
    }
}
